city = 'Pãshãwar'

# Encoding with different codecs
print(city.encode('utf_8'))       # b'S\xc3\xa3o Paulo'
print(city.encode('utf_16'))      # b'\xff\xfeS\x00\xe3\x00o\x00 \x00P\x00a\x00u\x00l\x00o\x00'
print(city.encode('iso8859_1'))   # b'S\xe3o Paulo'

# Encoding with cp437 codec without error handling
try:
    print(city.encode('cp437'))
except UnicodeEncodeError as e:
    print(e)  # UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in position 1: character maps to <undefined>

# Encoding with cp437 codec and different error handling strategies
print(city.encode('cp437', errors='ignore'))           # b'So Paulo'
print(city.encode('cp437', errors='replace'))          # b'S?o Paulo'
print(city.encode('cp437', errors='xmlcharrefreplace'))# b'S&#227;o Paulo
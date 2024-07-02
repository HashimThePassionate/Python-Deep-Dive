octets = b'Montr\xe9al'

# Decoding with different codecs
print(octets.decode('cp1252'))       # 'Montréal'
print(octets.decode('iso8859_7'))    # 'Montrιal'
print(octets.decode('koi8_r'))       # 'MontrИal'

# Decoding with utf_8 without error handling
try:
    print(octets.decode('utf_8'))
except UnicodeDecodeError as e:
    print(e)  # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 5: invalid continuation byte

# Decoding with utf_8 using 'replace' error handling
print(octets.decode('utf_8', errors='replace'))  # 'Montr�al'
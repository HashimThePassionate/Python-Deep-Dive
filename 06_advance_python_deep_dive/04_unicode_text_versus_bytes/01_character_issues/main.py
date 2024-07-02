s = 'café'
print(s)
print(len(s))  # Output: 4

print('Encoding to UTF8')
b = s.encode('utf8')
print(b)  # Output: b'caf\xc3\xa9'
print(len(b))  # Output: 5

print('Decoding from UTF8')
decoded_s = b.decode('utf8')
print(decoded_s)  # Output: 'café'

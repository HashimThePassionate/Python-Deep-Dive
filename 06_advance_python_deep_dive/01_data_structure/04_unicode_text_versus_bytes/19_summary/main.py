# Sample text
text = "Hello, Hashim!"

# Encoding to bytes
encoded_text = text.encode('utf-8')
print(f'Encoded: {encoded_text}')

# Decoding back to string
decoded_text = encoded_text.decode('utf-8')
print(f'Decoded: {decoded_text}')


import chardet

# Sample byte sequence
byte_data = b'\xe4\xbd\xa0\xe5\xa5\xbd'

# Detect encoding
print('chardet')
result = chardet.detect(byte_data)
print(f'Encoding: {result["encoding"]}, Confidence: {result["confidence"]}')

# Sample text with BOM
bom_text = b'\xef\xbb\xbfHello, Hashim!'

# Detect and remove BOM
if bom_text.startswith(b'\xef\xbb\xbf'):
    bom_text = bom_text[3:]
print(bom_text.decode('utf-8'))


import sys

# Detect default encoding
default_encoding = sys.getdefaultencoding()
print(f'Default Encoding: {default_encoding}')

# Detect filesystem encoding
filesystem_encoding = sys.getfilesystemencoding()
print(f'Filesystem Encoding: {filesystem_encoding}')

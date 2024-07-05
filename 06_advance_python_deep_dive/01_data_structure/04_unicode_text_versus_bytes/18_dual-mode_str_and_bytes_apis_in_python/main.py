import os
import re

# Compile regular expressions for str and bytes
re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r'\w+')
re_numbers_bytes = re.compile(rb'\d+')
re_words_bytes = re.compile(rb'\w+')

# Unicode text containing Tamil digits and the name 'Hashim'
text_str = ("Hashim saw \u0be7\u0bed\u0be8\u0bef as 1729 = 1³ + 12³ = 9³ + 10³.")
text_bytes = text_str.encode('utf_8')
print(text_bytes)

# Print text in both formats
print(f'Text\n {text_str!r}')
print('Numbers')
print(' str :', re_numbers_str.findall(text_str))
print(' bytes:', re_numbers_bytes.findall(text_bytes))
print('Words')
print(' str :', re_words_str.findall(text_str))
print(' bytes:', re_words_bytes.findall(text_bytes))



# Compile regular expressions with re.ASCII flag
re_numbers_ascii = re.compile(r'\d+', re.ASCII)
re_words_ascii = re.compile(r'\w+', re.ASCII)

# Text containing Unicode and ASCII characters
text_str = "Hashim saw 123 and \u0be7\u0bed\u0be8\u0bef."

# Print ASCII-only matches
print('Numbers (ASCII-only)')
print(' str :', re_numbers_ascii.findall(text_str))
print('Words (ASCII-only)')
print(' str :', re_words_ascii.findall(text_str))



# List directory contents with str argument
print('List directory contents with str argument')
print(os.listdir('.'))

# List directory contents with bytes argument
print('List directory contents with bytes argument')
print(os.listdir(b'.'))




# Encode a str to bytes
encoded_path = os.fsencode('digits-of-π.txt')
print(f'Encoded: {encoded_path}')

# Decode bytes to str
decoded_path = os.fsdecode(encoded_path)
print(f'Decoded: {decoded_path}')

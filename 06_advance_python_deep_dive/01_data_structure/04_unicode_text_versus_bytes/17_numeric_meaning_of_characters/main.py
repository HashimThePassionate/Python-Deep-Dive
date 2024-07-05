import unicodedata 
import re
re_digit = re.compile(r'\d')
sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'
for char in sample:
    print(f'U+{ord(char):04x}',
          char.center(6),
          're_dig' if re_digit.match(char) else '-',
          'isdig' if char.isdigit() else '-',
          'isnum' if char.isnumeric() else '-',
          f'{unicodedata.numeric(char):5.2f}',
          unicodedata.name(char),
          sep='\t')



# convert a character to its unicode code point
# char = '㊅'
# unicode_code_point = ord(char)  # 12933
# print(unicode_code_point)
# formatted_code_point = f'U+{unicode_code_point:04x}'  # U+3285
# print(formatted_code_point)
# print(chr(unicode_code_point))




from unicodedata import name

micro = 'µ'
print(name(micro))  # Output: 'MICRO SIGN'

micro_cf = micro.casefold()
print(name(micro_cf))  # Output: 'GREEK SMALL LETTER MU'

print(micro, micro_cf)  # Output: ('µ', 'μ')



from unicodedata import name

eszett = 'ß'
print(name(eszett))  # Output: 'LATIN SMALL LETTER SHARP S'

eszett_cf = eszett.casefold()
print(eszett, eszett_cf)  # Output: ('ß', 'ss')
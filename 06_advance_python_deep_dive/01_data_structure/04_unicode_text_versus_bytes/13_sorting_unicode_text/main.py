import locale

# Set locale to Brazilian Portuguese
my_locale = locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
print(my_locale)  # Output: 'pt_BR.UTF-8'

fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=locale.strxfrm)
print(sorted_fruits)
# Output: ['açaí', 'acerola', 'atemoia', 'cajá', 'caju']
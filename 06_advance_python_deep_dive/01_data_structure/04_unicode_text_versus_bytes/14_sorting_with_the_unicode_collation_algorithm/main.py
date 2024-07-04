import pyuca

coll = pyuca.Collator()
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=coll.sort_key)
print(sorted_fruits)
# Output: ['açaí', 'acerola', 'atemoia', 'cajá', 'caju']
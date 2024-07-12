class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return f'Cheese({self.kind!r})'

import weakref

stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese

print(sorted(stock.keys()))  # Output: ['Brie', 'Parmesan', 'Red Leicester', 'Tilsit']

del catalog
print(sorted(stock.keys()))  # Output: ['Parmesan']

del cheese
print(sorted(stock.keys()))  # Output: []
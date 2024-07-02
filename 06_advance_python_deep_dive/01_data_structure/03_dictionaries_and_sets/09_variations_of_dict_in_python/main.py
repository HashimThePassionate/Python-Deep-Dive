from collections import OrderedDict

# Creating two OrderedDicts
od1 = OrderedDict([('a', 1), ('b', 2)])
od2 = OrderedDict([('b', 2), ('a', 1)])

# Equality check (order matters)
print(od1 == od2)  # Output: False

od3 = OrderedDict([('a', 1), ('b', 2)])
print(od1 == od3)  # Output: True


od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Popping items
print(od.popitem())  # Output: ('c', 3)
print(od.popitem(last=False))  # Output: ('a', 1)



od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Move 'a' to the end
od.move_to_end('a')
print(od)  # Output: OrderedDict([('b', 2), ('c', 3), ('a', 1)])

# Move 'b' to the start
od.move_to_end('b', last=False)
print(od)  # Output: OrderedDict([('b', 2), ('c', 3), ('a', 1)])


# Creating an OrderedDict
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Accessing items
print(od['a'])  # Output: 1

# Adding and reordering items
# od['d'] = 4
od.move_to_end('a')
print(od)  # Output: OrderedDict([('b', 2), ('c', 3), ('d', 4), ('a', 1)])



from collections import ChainMap

# Creating dictionaries
d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}

# Creating a ChainMap
chain = ChainMap(d1, d2)

# Accessing items
print(chain['a'])  # Output: 1 (from d1)
print(chain['c'])  # Output: 6 (from d2)


# Updating items in ChainMap
chain['c'] = -1
print(d1)  # Output: {'a': 1, 'b': 3, 'c': -1}
print(d2)  # Output: {'a': 2, 'b': 4, 'c': 6}


from collections import Counter

# Counting letters in a word
ct = Counter('abracadabra')
print(ct)  # Output: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# Updating counts
ct.update('aaaaazzz')
print(ct)  # Output: Counter({'a': 10, 'z': 3, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# Most common items
print(ct.most_common(3))  # Output: [('a', 10), ('z', 3), ('b', 2)]


import shelve

# Creating and using a shelf
with shelve.open('my_shelf.db') as shelf:
    shelf['key'] = 'value'
    print(shelf['key'])  # Output: value

# The shelf is automatically closed when exiting the with block


import collections

class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

# Creating an object of StrKeyDict
d = StrKeyDict([('2', 'two'), ('4', 'four')])

# Accessing items
print(d[4])  # Output: 'four' (4 is converted to '4')

# Checking membership
print(2 in d)  # Output: True (2 is converted to '2')

# Setting items
d[1] = 'one'
print(d['1'])  # Output: 'one'
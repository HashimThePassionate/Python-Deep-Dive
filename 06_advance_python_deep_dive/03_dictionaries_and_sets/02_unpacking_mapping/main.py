# Function that accepts any number of keyword arguments and returns them as a dictionary
def dump(**kwargs):
    return kwargs

# Calling the dump function with multiple keyword arguments
# The ** syntax is used to unpack dictionaries into keyword arguments
print(dump(**{'x': 1}, y=2, **{'z': 3}))

# Combining multiple dictionaries and individual key-value pairs into a single dictionary
print({'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}})

# Merging dictionaries using the | (pipe) operator (Python 3.9+ feature)
d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}
print(d1 | d2)

# Merging dictionaries using the |= (in-place pipe) operator (Python 3.9+ feature)
d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}
d1 |= d2
print(d1)
